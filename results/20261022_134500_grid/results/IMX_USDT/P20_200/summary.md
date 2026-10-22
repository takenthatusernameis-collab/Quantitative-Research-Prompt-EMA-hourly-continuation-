# EMA Hourly Continuation — IMX/USDT P20_200

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8210 |
| net_win_rate | 0.5187 |
| gross_profit_factor | 1.1333 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -0.9836 |
| sortino_ratio | -0.2700 |
| max_drawdown | 0.3738 |
| cagr | -0.1216 |
| net_avg_win | 65.9478 |
| net_avg_loss | -86.5756 |
| avg_hold_time_bars | 38.4866 |
| exposure | 0.6513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
