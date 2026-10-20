# EMA Hourly Continuation — AMP/USDT P34_89

**Symbol:** AMP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.3583 |
| net_win_rate | 0.3709 |
| gross_profit_factor | 0.6611 |
| gross_win_rate | 0.3819 |
| sharpe_ratio | -10.6282 |
| sortino_ratio | -4.7467 |
| max_drawdown | 0.9976 |
| cagr | -0.9077 |
| net_avg_win | 15.0930 |
| net_avg_loss | -24.8308 |
| avg_hold_time_bars | 6.1477 |
| exposure | 0.2780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
