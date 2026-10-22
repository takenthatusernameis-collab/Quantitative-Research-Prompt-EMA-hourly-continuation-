# EMA Hourly Continuation — FIL/USDT P8_50

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1088 |
| net_profit_factor | 0.5198 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9578 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -6.5107 |
| sortino_ratio | -3.0038 |
| max_drawdown | 0.9761 |
| cagr | -0.7711 |
| net_avg_win | 20.8253 |
| net_avg_loss | -34.9600 |
| avg_hold_time_bars | 9.7233 |
| exposure | 0.4809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
