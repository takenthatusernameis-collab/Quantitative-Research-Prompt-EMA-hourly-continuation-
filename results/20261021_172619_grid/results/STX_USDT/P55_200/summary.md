# EMA Hourly Continuation — STX/USDT P55_200

**Symbol:** STX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.7717 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9404 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.2006 |
| sortino_ratio | -0.2788 |
| max_drawdown | 0.3032 |
| cagr | -0.1208 |
| net_avg_win | 71.5180 |
| net_avg_loss | -89.9340 |
| avg_hold_time_bars | 31.3684 |
| exposure | 0.3776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
