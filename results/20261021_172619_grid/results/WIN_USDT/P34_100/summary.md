# EMA Hourly Continuation — WIN/USDT P34_100

**Symbol:** WIN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7142 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0069 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.9923 |
| sortino_ratio | -0.5435 |
| max_drawdown | 0.5006 |
| cagr | -0.2208 |
| net_avg_win | 64.2865 |
| net_avg_loss | -90.5066 |
| avg_hold_time_bars | 16.0970 |
| exposure | 0.2641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
