# EMA Hourly Continuation — ZEC/USDT P21_144

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 1.0280 |
| net_win_rate | 0.5492 |
| gross_profit_factor | 1.2118 |
| gross_win_rate | 0.5492 |
| sharpe_ratio | 0.2261 |
| sortino_ratio | 0.0628 |
| max_drawdown | 0.1664 |
| cagr | 0.0202 |
| net_avg_win | 93.7805 |
| net_avg_loss | -111.1265 |
| avg_hold_time_bars | 30.8115 |
| exposure | 0.5126 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
