# EMA Hourly Continuation — KNC/USDT P12_144

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8967 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1180 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.5560 |
| sortino_ratio | -0.1402 |
| max_drawdown | 0.2577 |
| cagr | -0.0652 |
| net_avg_win | 83.4906 |
| net_avg_loss | -104.7444 |
| avg_hold_time_bars | 54.4216 |
| exposure | 0.7570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
