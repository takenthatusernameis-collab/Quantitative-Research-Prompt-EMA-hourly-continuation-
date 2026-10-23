# EMA Hourly Continuation — AMP/USDT P12_144

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.3315 |
| net_win_rate | 0.3786 |
| gross_profit_factor | 0.5484 |
| gross_win_rate | 0.3843 |
| sharpe_ratio | -8.6349 |
| sortino_ratio | -3.5912 |
| max_drawdown | 0.9887 |
| cagr | -0.8296 |
| net_avg_win | 14.7584 |
| net_avg_loss | -27.1235 |
| avg_hold_time_bars | 15.1938 |
| exposure | 0.6057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
