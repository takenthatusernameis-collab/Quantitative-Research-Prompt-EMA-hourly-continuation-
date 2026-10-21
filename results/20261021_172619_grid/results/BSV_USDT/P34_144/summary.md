# EMA Hourly Continuation — BSV/USDT P34_144

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5774 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.7467 |
| gross_win_rate | 0.4175 |
| sharpe_ratio | -3.7026 |
| sortino_ratio | -1.0459 |
| max_drawdown | 0.7090 |
| cagr | -0.3834 |
| net_avg_win | 57.5288 |
| net_avg_loss | -71.4074 |
| avg_hold_time_bars | 22.2175 |
| exposure | 0.4040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
