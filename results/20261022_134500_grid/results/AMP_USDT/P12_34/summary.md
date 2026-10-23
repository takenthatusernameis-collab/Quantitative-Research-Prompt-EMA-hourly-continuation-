# EMA Hourly Continuation — AMP/USDT P12_34

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1675 |
| net_profit_factor | 0.2930 |
| net_win_rate | 0.3606 |
| gross_profit_factor | 0.6657 |
| gross_win_rate | 0.3851 |
| sharpe_ratio | -15.3311 |
| sortino_ratio | -8.9046 |
| max_drawdown | 1.0000 |
| cagr | -0.9895 |
| net_avg_win | 6.8615 |
| net_avg_loss | -13.2065 |
| avg_hold_time_bars | 3.5672 |
| exposure | 0.2716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
