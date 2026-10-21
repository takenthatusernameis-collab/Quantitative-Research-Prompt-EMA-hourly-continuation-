# EMA Hourly Continuation — ONE/USDT P20_55

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7823 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.7036 |
| sortino_ratio | -0.5382 |
| max_drawdown | 0.5201 |
| cagr | -0.2201 |
| net_avg_win | 68.9761 |
| net_avg_loss | -87.4435 |
| avg_hold_time_bars | 10.3539 |
| exposure | 0.2287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
