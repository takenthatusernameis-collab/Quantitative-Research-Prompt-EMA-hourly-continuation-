# EMA Hourly Continuation — AKT/USDT P50_55

**Symbol:** AKT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 815 |
| net_profit_factor | 0.2330 |
| net_win_rate | 0.3853 |
| gross_profit_factor | 0.7189 |
| gross_win_rate | 0.4196 |
| sharpe_ratio | -11.2246 |
| sortino_ratio | -4.6524 |
| max_drawdown | 0.9981 |
| cagr | -0.9176 |
| net_avg_win | 9.6580 |
| net_avg_loss | -25.9754 |
| avg_hold_time_bars | 2.0675 |
| exposure | 0.0766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
