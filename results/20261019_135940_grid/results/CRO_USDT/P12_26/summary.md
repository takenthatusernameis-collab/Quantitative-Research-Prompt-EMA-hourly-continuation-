# EMA Hourly Continuation — CRO/USDT P12_26

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1440 |
| net_profit_factor | 0.2604 |
| net_win_rate | 0.3722 |
| gross_profit_factor | 0.8352 |
| gross_win_rate | 0.4215 |
| sharpe_ratio | -15.0373 |
| sortino_ratio | -8.2259 |
| max_drawdown | 1.0000 |
| cagr | -0.9867 |
| net_avg_win | 6.5669 |
| net_avg_loss | -14.9554 |
| avg_hold_time_bars | 3.1035 |
| exposure | 0.2031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
