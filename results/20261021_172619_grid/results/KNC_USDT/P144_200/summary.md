# EMA Hourly Continuation — KNC/USDT P144_200

**Symbol:** KNC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.7583 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1386 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | -1.3144 |
| sortino_ratio | -0.2931 |
| max_drawdown | 0.3129 |
| cagr | -0.1257 |
| net_avg_win | 71.2646 |
| net_avg_loss | -105.7320 |
| avg_hold_time_bars | 7.9328 |
| exposure | 0.0858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
