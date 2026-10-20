# EMA Hourly Continuation — ETN/USDT P12_55

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.3918 |
| net_win_rate | 0.3660 |
| gross_profit_factor | 0.5879 |
| gross_win_rate | 0.3787 |
| sharpe_ratio | -10.5601 |
| sortino_ratio | -5.0028 |
| max_drawdown | 0.9945 |
| cagr | -0.9154 |
| net_avg_win | 18.4608 |
| net_avg_loss | -27.2050 |
| avg_hold_time_bars | 6.8259 |
| exposure | 0.3515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
