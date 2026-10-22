# EMA Hourly Continuation — WLD/USDT P50_55

**Symbol:** WLD/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.2736 |
| net_win_rate | 0.3774 |
| gross_profit_factor | 0.6829 |
| gross_win_rate | 0.4043 |
| sharpe_ratio | -10.5191 |
| sortino_ratio | -4.1306 |
| max_drawdown | 0.9964 |
| cagr | -0.8927 |
| net_avg_win | 13.4020 |
| net_avg_loss | -29.6878 |
| avg_hold_time_bars | 1.8962 |
| exposure | 0.0640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
