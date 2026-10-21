# EMA Hourly Continuation — GMX/USDT P12_144

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7192 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8843 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -2.2784 |
| sortino_ratio | -0.6914 |
| max_drawdown | 0.5767 |
| cagr | -0.2734 |
| net_avg_win | 66.0326 |
| net_avg_loss | -80.8512 |
| avg_hold_time_bars | 30.7943 |
| exposure | 0.6397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
