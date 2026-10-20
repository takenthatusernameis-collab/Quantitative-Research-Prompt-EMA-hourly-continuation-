# EMA Hourly Continuation — AMP/USDT P50_55

**Symbol:** AMP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1128 |
| net_profit_factor | 0.1794 |
| net_win_rate | 0.2775 |
| gross_profit_factor | 0.5848 |
| gross_win_rate | 0.3564 |
| sharpe_ratio | -17.1059 |
| sortino_ratio | -8.6467 |
| max_drawdown | 1.0000 |
| cagr | -0.9914 |
| net_avg_win | 6.9830 |
| net_avg_loss | -14.9517 |
| avg_hold_time_bars | 2.0878 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
