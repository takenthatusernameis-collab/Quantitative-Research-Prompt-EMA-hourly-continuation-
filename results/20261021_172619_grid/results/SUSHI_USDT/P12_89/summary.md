# EMA Hourly Continuation — SUSHI/USDT P12_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -2.5535 |
| sortino_ratio | -0.8013 |
| max_drawdown | 0.6152 |
| cagr | -0.3085 |
| net_avg_win | 66.2876 |
| net_avg_loss | -79.6903 |
| avg_hold_time_bars | 24.6653 |
| exposure | 0.5469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
