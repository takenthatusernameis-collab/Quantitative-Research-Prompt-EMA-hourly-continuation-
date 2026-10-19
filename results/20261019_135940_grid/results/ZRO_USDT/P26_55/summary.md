# EMA Hourly Continuation — ZRO/USDT P26_55

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 880 |
| net_profit_factor | 0.6518 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0513 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -4.6981 |
| sortino_ratio | -2.0302 |
| max_drawdown | 0.9027 |
| cagr | -0.6262 |
| net_avg_win | 38.4247 |
| net_avg_loss | -58.4212 |
| avg_hold_time_bars | 4.3795 |
| exposure | 0.1886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
