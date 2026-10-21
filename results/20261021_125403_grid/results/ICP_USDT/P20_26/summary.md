# EMA Hourly Continuation — ICP/USDT P20_26

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 144 |
| net_profit_factor | 0.6497 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9193 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.6125 |
| sortino_ratio | -0.2774 |
| max_drawdown | 0.2989 |
| cagr | -0.1195 |
| net_avg_win | 73.5285 |
| net_avg_loss | -104.1112 |
| avg_hold_time_bars | 4.1944 |
| exposure | 0.0275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
