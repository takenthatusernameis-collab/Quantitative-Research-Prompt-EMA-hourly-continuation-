# EMA Hourly Continuation — XYO/USDT P20_26

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1307 |
| net_profit_factor | 0.1771 |
| net_win_rate | 0.3175 |
| gross_profit_factor | 0.6585 |
| gross_win_rate | 0.3695 |
| sharpe_ratio | -16.7985 |
| sortino_ratio | -8.9680 |
| max_drawdown | 1.0000 |
| cagr | -0.9914 |
| net_avg_win | 5.1850 |
| net_avg_loss | -13.6230 |
| avg_hold_time_bars | 2.4170 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
