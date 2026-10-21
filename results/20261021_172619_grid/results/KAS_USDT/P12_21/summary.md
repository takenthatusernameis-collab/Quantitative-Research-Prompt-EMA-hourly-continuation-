# EMA Hourly Continuation — KAS/USDT P12_21

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.9320 |
| net_win_rate | 0.5669 |
| gross_profit_factor | 1.2964 |
| gross_win_rate | 0.5669 |
| sharpe_ratio | -0.3169 |
| sortino_ratio | -0.0737 |
| max_drawdown | 0.2466 |
| cagr | -0.0362 |
| net_avg_win | 84.2223 |
| net_avg_loss | -118.3002 |
| avg_hold_time_bars | 4.7047 |
| exposure | 0.0543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
