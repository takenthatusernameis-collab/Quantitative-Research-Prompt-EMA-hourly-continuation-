# EMA Hourly Continuation — WLD/USDT P50_200

**Symbol:** WLD/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.8429 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9570 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -0.7888 |
| sortino_ratio | -0.1752 |
| max_drawdown | 0.2371 |
| cagr | -0.0792 |
| net_avg_win | 84.3415 |
| net_avg_loss | -96.8097 |
| avg_hold_time_bars | 37.0413 |
| exposure | 0.4075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
