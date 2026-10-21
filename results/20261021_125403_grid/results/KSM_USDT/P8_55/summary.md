# EMA Hourly Continuation — KSM/USDT P8_55

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -2.8719 |
| sortino_ratio | -1.0808 |
| max_drawdown | 0.7162 |
| cagr | -0.3915 |
| net_avg_win | 50.5568 |
| net_avg_loss | -65.8325 |
| avg_hold_time_bars | 15.0000 |
| exposure | 0.4752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
