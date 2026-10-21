# EMA Hourly Continuation — ETH/USDT P20_200

**Symbol:** ETH/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.6777 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9188 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.6435 |
| sortino_ratio | -0.3333 |
| max_drawdown | 0.3505 |
| cagr | -0.1422 |
| net_avg_win | 68.6150 |
| net_avg_loss | -95.4016 |
| avg_hold_time_bars | 77.2277 |
| exposure | 0.7091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
