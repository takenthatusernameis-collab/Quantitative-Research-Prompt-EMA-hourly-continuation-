# EMA Hourly Continuation — KNC/USDT P89_200

**Symbol:** KNC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6165 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9844 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.9863 |
| sortino_ratio | -0.7805 |
| max_drawdown | 0.6490 |
| cagr | -0.3204 |
| net_avg_win | 58.0366 |
| net_avg_loss | -89.9541 |
| avg_hold_time_bars | 13.2358 |
| exposure | 0.2118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
