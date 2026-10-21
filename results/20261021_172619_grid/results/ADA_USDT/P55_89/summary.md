# EMA Hourly Continuation — ADA/USDT P55_89

**Symbol:** ADA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7209 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0169 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.5096 |
| sortino_ratio | -0.3619 |
| max_drawdown | 0.3510 |
| cagr | -0.1524 |
| net_avg_win | 61.8003 |
| net_avg_loss | -90.1732 |
| avg_hold_time_bars | 6.9892 |
| exposure | 0.0880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
