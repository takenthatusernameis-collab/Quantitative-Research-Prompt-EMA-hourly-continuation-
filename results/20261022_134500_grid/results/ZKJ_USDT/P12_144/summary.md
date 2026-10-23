# EMA Hourly Continuation — ZKJ/USDT P12_144

**Symbol:** ZKJ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.2302 |
| net_win_rate | 0.3443 |
| gross_profit_factor | 0.5920 |
| gross_win_rate | 0.4139 |
| sharpe_ratio | -6.6631 |
| sortino_ratio | -1.6009 |
| max_drawdown | 0.8866 |
| cagr | -0.5740 |
| net_avg_win | 28.0757 |
| net_avg_loss | -64.0566 |
| avg_hold_time_bars | 69.9560 |
| exposure | 0.8681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
