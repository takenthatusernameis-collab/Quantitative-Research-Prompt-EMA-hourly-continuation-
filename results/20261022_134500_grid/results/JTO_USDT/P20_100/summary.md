# EMA Hourly Continuation — JTO/USDT P20_100

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.6929 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9476 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -3.2061 |
| sortino_ratio | -1.1660 |
| max_drawdown | 0.7597 |
| cagr | -0.4227 |
| net_avg_win | 53.4246 |
| net_avg_loss | -70.0146 |
| avg_hold_time_bars | 14.2786 |
| exposure | 0.4310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
