# EMA Hourly Continuation — DUSK/USDT P21_200

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7628 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.5687 |
| sortino_ratio | -0.4267 |
| max_drawdown | 0.4457 |
| cagr | -0.1805 |
| net_avg_win | 70.6720 |
| net_avg_loss | -88.6870 |
| avg_hold_time_bars | 37.0656 |
| exposure | 0.6166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
