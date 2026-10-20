# EMA Hourly Continuation — ONT/USDT P144_200

**Symbol:** ONT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.4050 |
| net_win_rate | 0.4162 |
| gross_profit_factor | 0.7739 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -5.1930 |
| sortino_ratio | -1.4403 |
| max_drawdown | 0.8371 |
| cagr | -0.5016 |
| net_avg_win | 35.4254 |
| net_avg_loss | -62.3617 |
| avg_hold_time_bars | 3.8874 |
| exposure | 0.0672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
