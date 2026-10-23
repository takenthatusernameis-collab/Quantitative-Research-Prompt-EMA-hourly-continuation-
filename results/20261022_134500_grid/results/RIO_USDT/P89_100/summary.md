# EMA Hourly Continuation — RIO/USDT P89_100

**Symbol:** RIO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.2475 |
| net_win_rate | 0.3003 |
| gross_profit_factor | 0.4785 |
| gross_win_rate | 0.3151 |
| sharpe_ratio | -11.1089 |
| sortino_ratio | -4.1936 |
| max_drawdown | 0.9955 |
| cagr | -0.8852 |
| net_avg_win | 16.1306 |
| net_avg_loss | -27.9673 |
| avg_hold_time_bars | 2.0621 |
| exposure | 0.0640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
