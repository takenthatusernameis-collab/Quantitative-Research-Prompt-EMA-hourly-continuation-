# EMA Hourly Continuation — ICP/USDT P89_100

**Symbol:** ICP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.1985 |
| net_win_rate | 0.3622 |
| gross_profit_factor | 0.5764 |
| gross_win_rate | 0.4038 |
| sharpe_ratio | -10.4164 |
| sortino_ratio | -3.7907 |
| max_drawdown | 0.9948 |
| cagr | -0.8758 |
| net_avg_win | 10.9016 |
| net_avg_loss | -31.1825 |
| avg_hold_time_bars | 1.8862 |
| exposure | 0.0535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
