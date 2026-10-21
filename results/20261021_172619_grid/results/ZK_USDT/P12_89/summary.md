# EMA Hourly Continuation — ZK/USDT P12_89

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.8180 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9837 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.5942 |
| sortino_ratio | -0.5404 |
| max_drawdown | 0.4783 |
| cagr | -0.2223 |
| net_avg_win | 77.1874 |
| net_avg_loss | -91.8835 |
| avg_hold_time_bars | 20.2000 |
| exposure | 0.5170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
