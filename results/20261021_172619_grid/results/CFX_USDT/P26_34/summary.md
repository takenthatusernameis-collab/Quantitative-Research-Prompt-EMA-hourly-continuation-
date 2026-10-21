# EMA Hourly Continuation — CFX/USDT P26_34

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 186 |
| net_profit_factor | 0.6915 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9839 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5305 |
| sortino_ratio | -0.3002 |
| max_drawdown | 0.3628 |
| cagr | -0.1280 |
| net_avg_win | 70.1603 |
| net_avg_loss | -101.4600 |
| avg_hold_time_bars | 5.4086 |
| exposure | 0.0457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
