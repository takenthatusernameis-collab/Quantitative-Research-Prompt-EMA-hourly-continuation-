# EMA Hourly Continuation — GTC/USDT P12_144

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6507 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.9093 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -3.0659 |
| sortino_ratio | -0.9770 |
| max_drawdown | 0.6942 |
| cagr | -0.3671 |
| net_avg_win | 53.2461 |
| net_avg_loss | -72.1618 |
| avg_hold_time_bars | 27.4137 |
| exposure | 0.6355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
