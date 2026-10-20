# EMA Hourly Continuation — BICO/USDT P8_89

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.7650 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0213 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -2.2643 |
| sortino_ratio | -0.8188 |
| max_drawdown | 0.6435 |
| cagr | -0.3186 |
| net_avg_win | 62.5218 |
| net_avg_loss | -80.7223 |
| avg_hold_time_bars | 22.7222 |
| exposure | 0.6693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
