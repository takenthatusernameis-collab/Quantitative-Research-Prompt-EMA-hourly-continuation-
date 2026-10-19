# EMA Hourly Continuation — CRV/USDT P8_50

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1063 |
| net_profit_factor | 0.6387 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -5.2041 |
| sortino_ratio | -2.3859 |
| max_drawdown | 0.9462 |
| cagr | -0.6821 |
| net_avg_win | 32.7139 |
| net_avg_loss | -47.2366 |
| avg_hold_time_bars | 9.5193 |
| exposure | 0.4600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
