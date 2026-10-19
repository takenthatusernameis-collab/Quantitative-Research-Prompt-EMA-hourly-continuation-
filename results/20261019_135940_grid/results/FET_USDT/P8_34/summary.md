# EMA Hourly Continuation — FET/USDT P8_34

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1451 |
| net_profit_factor | 0.5320 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -7.8543 |
| sortino_ratio | -4.2042 |
| max_drawdown | 0.9941 |
| cagr | -0.8708 |
| net_avg_win | 16.9677 |
| net_avg_loss | -27.0597 |
| avg_hold_time_bars | 4.9290 |
| exposure | 0.3251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
