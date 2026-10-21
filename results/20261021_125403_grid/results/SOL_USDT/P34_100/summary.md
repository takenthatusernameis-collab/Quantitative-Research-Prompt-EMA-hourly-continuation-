# EMA Hourly Continuation — SOL/USDT P34_100

**Symbol:** SOL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7520 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 1.0011 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.8255 |
| sortino_ratio | -0.5031 |
| max_drawdown | 0.4674 |
| cagr | -0.2065 |
| net_avg_win | 72.6107 |
| net_avg_loss | -95.5199 |
| avg_hold_time_bars | 12.7622 |
| exposure | 0.2146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
