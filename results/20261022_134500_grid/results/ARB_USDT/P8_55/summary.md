# EMA Hourly Continuation — ARB/USDT P8_55

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.5386 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9044 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -5.2989 |
| sortino_ratio | -2.3122 |
| max_drawdown | 0.9428 |
| cagr | -0.6781 |
| net_avg_win | 23.6458 |
| net_avg_loss | -40.0291 |
| avg_hold_time_bars | 11.7641 |
| exposure | 0.5214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
