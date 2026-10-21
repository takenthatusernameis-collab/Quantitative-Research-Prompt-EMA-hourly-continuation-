# EMA Hourly Continuation — BCH/USDT P34_55

**Symbol:** BCH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9438 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.4950 |
| sortino_ratio | -0.5934 |
| max_drawdown | 0.5109 |
| cagr | -0.2353 |
| net_avg_win | 60.9897 |
| net_avg_loss | -91.2173 |
| avg_hold_time_bars | 6.2847 |
| exposure | 0.0783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
