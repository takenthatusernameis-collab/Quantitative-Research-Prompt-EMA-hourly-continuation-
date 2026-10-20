# EMA Hourly Continuation — ANKR/USDT P50_100

**Symbol:** ANKR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.4724 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.8260 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -6.5863 |
| sortino_ratio | -2.3574 |
| max_drawdown | 0.9444 |
| cagr | -0.6814 |
| net_avg_win | 31.2887 |
| net_avg_loss | -48.5929 |
| avg_hold_time_bars | 7.8182 |
| exposure | 0.2267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
