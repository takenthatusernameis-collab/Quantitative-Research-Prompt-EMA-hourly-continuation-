# EMA Hourly Continuation — XPR/USDT P12_26

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.6606 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -2.1333 |
| sortino_ratio | -0.5058 |
| max_drawdown | 0.4825 |
| cagr | -0.2074 |
| net_avg_win | 64.6886 |
| net_avg_loss | -92.3749 |
| avg_hold_time_bars | 9.3978 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
