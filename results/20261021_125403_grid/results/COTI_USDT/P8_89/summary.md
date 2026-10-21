# EMA Hourly Continuation — COTI/USDT P8_89

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.9607 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1353 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | -0.2332 |
| sortino_ratio | -0.0791 |
| max_drawdown | 0.3183 |
| cagr | -0.0444 |
| net_avg_win | 89.6668 |
| net_avg_loss | -106.7731 |
| avg_hold_time_bars | 24.6207 |
| exposure | 0.6166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
