# EMA Hourly Continuation — TIA/USDT P12_144

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.8082 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9081 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -1.1449 |
| sortino_ratio | -0.2878 |
| max_drawdown | 0.3557 |
| cagr | -0.1256 |
| net_avg_win | 80.9445 |
| net_avg_loss | -91.5521 |
| avg_hold_time_bars | 48.3782 |
| exposure | 0.6861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
