# EMA Hourly Continuation — WLD/USDT P12_21

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.8092 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0585 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.0640 |
| sortino_ratio | -0.2372 |
| max_drawdown | 0.3165 |
| cagr | -0.1034 |
| net_avg_win | 82.6871 |
| net_avg_loss | -107.4173 |
| avg_hold_time_bars | 4.6042 |
| exposure | 0.0502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
