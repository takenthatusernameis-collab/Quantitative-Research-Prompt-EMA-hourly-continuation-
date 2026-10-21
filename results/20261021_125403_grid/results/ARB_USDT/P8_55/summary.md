# EMA Hourly Continuation — ARB/USDT P8_55

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.8232 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0273 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -1.3682 |
| sortino_ratio | -0.4812 |
| max_drawdown | 0.4692 |
| cagr | -0.2012 |
| net_avg_win | 65.6121 |
| net_avg_loss | -82.9527 |
| avg_hold_time_bars | 17.9950 |
| exposure | 0.4908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
