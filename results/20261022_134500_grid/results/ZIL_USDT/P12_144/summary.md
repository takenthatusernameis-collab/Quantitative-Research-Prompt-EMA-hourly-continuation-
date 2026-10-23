# EMA Hourly Continuation — ZIL/USDT P12_144

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6149 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -3.4401 |
| sortino_ratio | -1.0723 |
| max_drawdown | 0.7448 |
| cagr | -0.4013 |
| net_avg_win | 50.2738 |
| net_avg_loss | -71.7788 |
| avg_hold_time_bars | 30.5955 |
| exposure | 0.6842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
