# EMA Hourly Continuation — ILV/USDT P50_89

**Symbol:** ILV/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7052 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -2.1875 |
| sortino_ratio | -0.5884 |
| max_drawdown | 0.5011 |
| cagr | -0.2367 |
| net_avg_win | 68.8965 |
| net_avg_loss | -91.7936 |
| avg_hold_time_bars | 7.5779 |
| exposure | 0.1216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
