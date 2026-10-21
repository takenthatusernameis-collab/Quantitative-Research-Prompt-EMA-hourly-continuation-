# EMA Hourly Continuation — ZRO/USDT P21_100

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.8734 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0242 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -0.8312 |
| sortino_ratio | -0.2567 |
| max_drawdown | 0.2903 |
| cagr | -0.1150 |
| net_avg_win | 78.0868 |
| net_avg_loss | -92.7960 |
| avg_hold_time_bars | 18.7884 |
| exposure | 0.3954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
