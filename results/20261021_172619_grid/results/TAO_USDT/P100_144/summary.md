# EMA Hourly Continuation — TAO/USDT P100_144

**Symbol:** TAO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 173 |
| net_profit_factor | 0.6866 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8737 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -1.5709 |
| sortino_ratio | -0.2940 |
| max_drawdown | 0.2865 |
| cagr | -0.1258 |
| net_avg_win | 78.4706 |
| net_avg_loss | -98.3070 |
| avg_hold_time_bars | 6.3873 |
| exposure | 0.0502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
