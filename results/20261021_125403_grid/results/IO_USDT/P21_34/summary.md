# EMA Hourly Continuation — IO/USDT P21_34

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.8597 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0959 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.7907 |
| sortino_ratio | -0.1897 |
| max_drawdown | 0.2164 |
| cagr | -0.0850 |
| net_avg_win | 85.0937 |
| net_avg_loss | -108.5653 |
| avg_hold_time_bars | 5.2615 |
| exposure | 0.0662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
