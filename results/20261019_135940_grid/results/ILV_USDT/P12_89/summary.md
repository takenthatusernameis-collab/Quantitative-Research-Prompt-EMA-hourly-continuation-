# EMA Hourly Continuation — ILV/USDT P12_89

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.6908 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -3.7392 |
| sortino_ratio | -1.4400 |
| max_drawdown | 0.8260 |
| cagr | -0.4959 |
| net_avg_win | 50.5314 |
| net_avg_loss | -68.9667 |
| avg_hold_time_bars | 14.7139 |
| exposure | 0.5003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
